# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TFIM_METADATA = Metadata(
    id="e112b845a4c25dd82a06881f7a7a51dae6274c19.boutiques",
    name="tfim",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


TfimParameters = typing.TypedDict('TfimParameters', {
    "__STYX_TYPE__": typing.Literal["tfim"],
    "prefix": typing.NotRequired[str | None],
    "pthresh": typing.NotRequired[float | None],
    "eqcorr": typing.NotRequired[float | None],
    "paired": bool,
    "set1_images": list[InputPathType],
    "set2_images": list[InputPathType],
    "base1_value": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "tfim": tfim_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "tfim": tfim_outputs,
    }.get(t)


class TfimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tfim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    diff_output: OutputPathType | None
    """Difference image output. Default prefix is 'tfim'."""
    tspm_output: OutputPathType | None
    """T-statistic of difference. Default prefix is 'tfim'."""
    corr_output: OutputPathType | None
    """Equivalent correlation statistic output. Written if -eqcorr is used."""


def tfim_params(
    set1_images: list[InputPathType],
    set2_images: list[InputPathType],
    prefix: str | None = None,
    pthresh: float | None = None,
    eqcorr: float | None = None,
    paired: bool = False,
    base1_value: float | None = None,
) -> TfimParameters:
    """
    Build parameters.
    
    Args:
        set1_images: First set of image files.
        set2_images: Second set of image files.
        prefix: Prefix for output filenames. Default is 'tfim'.
        pthresh: Significance level (per voxel) to threshold the output with.\
            Voxels with t-statistic less significant than this will have their diff\
            output zeroed. Default is no threshold.
        eqcorr: Write out the equivalent correlation statistic. The number\
            'dval' is the value to use for 'dof'. Default is not to write this\
            file.
        paired: Compare -set1 and -set2 using a paired sample t-test. Illegal\
            with the -base1 option.
        base1_value: Base value for the first set of images. Used for Usage 2.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tfim",
        "paired": paired,
        "set1_images": set1_images,
        "set2_images": set2_images,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if pthresh is not None:
        params["pthresh"] = pthresh
    if eqcorr is not None:
        params["eqcorr"] = eqcorr
    if base1_value is not None:
        params["base1_value"] = base1_value
    return params


def tfim_cargs(
    params: TfimParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("tfim")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("pthresh") is not None:
        cargs.extend([
            "-pthresh",
            str(params.get("pthresh"))
        ])
    if params.get("eqcorr") is not None:
        cargs.extend([
            "-eqcorr",
            str(params.get("eqcorr"))
        ])
    if params.get("paired"):
        cargs.append("-paired")
    cargs.extend([
        "-set1",
        *[execution.input_file(f) for f in params.get("set1_images")]
    ])
    cargs.extend([
        "-set2",
        *[execution.input_file(f) for f in params.get("set2_images")]
    ])
    if params.get("base1_value") is not None:
        cargs.extend([
            "-base1",
            str(params.get("base1_value"))
        ])
    return cargs


def tfim_outputs(
    params: TfimParameters,
    execution: Execution,
) -> TfimOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TfimOutputs(
        root=execution.output_file("."),
        diff_output=execution.output_file(params.get("prefix") + ".diff") if (params.get("prefix") is not None) else None,
        tspm_output=execution.output_file(params.get("prefix") + ".tspm") if (params.get("prefix") is not None) else None,
        corr_output=execution.output_file(params.get("prefix") + ".corr") if (params.get("prefix") is not None) else None,
    )
    return ret


def tfim_execute(
    params: TfimParameters,
    execution: Execution,
) -> TfimOutputs:
    """
    MCW TFIM: t-tests on sets of functional images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TfimOutputs`).
    """
    params = execution.params(params)
    cargs = tfim_cargs(params, execution)
    ret = tfim_outputs(params, execution)
    execution.run(cargs)
    return ret


def tfim(
    set1_images: list[InputPathType],
    set2_images: list[InputPathType],
    prefix: str | None = None,
    pthresh: float | None = None,
    eqcorr: float | None = None,
    paired: bool = False,
    base1_value: float | None = None,
    runner: Runner | None = None,
) -> TfimOutputs:
    """
    MCW TFIM: t-tests on sets of functional images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        set1_images: First set of image files.
        set2_images: Second set of image files.
        prefix: Prefix for output filenames. Default is 'tfim'.
        pthresh: Significance level (per voxel) to threshold the output with.\
            Voxels with t-statistic less significant than this will have their diff\
            output zeroed. Default is no threshold.
        eqcorr: Write out the equivalent correlation statistic. The number\
            'dval' is the value to use for 'dof'. Default is not to write this\
            file.
        paired: Compare -set1 and -set2 using a paired sample t-test. Illegal\
            with the -base1 option.
        base1_value: Base value for the first set of images. Used for Usage 2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TfimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TFIM_METADATA)
    params = tfim_params(
        prefix=prefix,
        pthresh=pthresh,
        eqcorr=eqcorr,
        paired=paired,
        set1_images=set1_images,
        set2_images=set2_images,
        base1_value=base1_value,
    )
    return tfim_execute(params, execution)


__all__ = [
    "TFIM_METADATA",
    "TfimOutputs",
    "TfimParameters",
    "tfim",
    "tfim_params",
]
