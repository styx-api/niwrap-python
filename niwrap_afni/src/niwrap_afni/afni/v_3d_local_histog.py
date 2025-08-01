# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_LOCAL_HISTOG_METADATA = Metadata(
    id="a76400adcb984e82c7f568b9ba39dc70fabc3b25.boutiques",
    name="3dLocalHistog",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dLocalHistogParameters = typing.TypedDict('V3dLocalHistogParameters', {
    "__STYXTYPE__": typing.Literal["3dLocalHistog"],
    "nbhd_option": typing.NotRequired[str | None],
    "prefix": str,
    "hsave": typing.NotRequired[str | None],
    "lab_file": typing.NotRequired[InputPathType | None],
    "exclude": typing.NotRequired[list[str] | None],
    "exc_nonlab": bool,
    "mincount": typing.NotRequired[float | None],
    "probability": bool,
    "quiet": bool,
    "input_datasets": list[InputPathType],
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
        "3dLocalHistog": v_3d_local_histog_cargs,
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
        "3dLocalHistog": v_3d_local_histog_outputs,
    }.get(t)


class V3dLocalHistogOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_histog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_head: OutputPathType
    """The output dataset with the specified prefix"""
    output_dataset_brik: OutputPathType
    """The output dataset with the specified prefix"""
    histogram_file: OutputPathType | None
    """The overall histogram saved into the specified file"""


def v_3d_local_histog_params(
    prefix: str,
    input_datasets: list[InputPathType],
    nbhd_option: str | None = None,
    hsave: str | None = None,
    lab_file: InputPathType | None = None,
    exclude: list[str] | None = None,
    exc_nonlab: bool = False,
    mincount: float | None = None,
    probability: bool = False,
    quiet: bool = False,
) -> V3dLocalHistogParameters:
    """
    Build parameters.
    
    Args:
        prefix: Use string 'ppp' as the prefix for the output dataset.
        input_datasets: Input dataset(s) for the 3dLocalHistog tool.
        nbhd_option: Defines the region around each voxel to be used for the\
            statistics calculation. Available formats: 'SPHERE(r)', 'RECT(a,b,c)',\
            'RHDD(a)', 'TOHD(a)'.
        hsave: Save the overall histogram into file 'sss'. This file will have\
            2 columns: value and count.
        lab_file: Use file 'LL' as a label file.
        exclude: Exclude values from 'a' to 'b' from the counting. This option\
            can be used more than once.
        exc_nonlab: If '-lab_file' is used, then exclude all values that are\
            NOT in the label file (except for 0).
        mincount: Exclude values which appear in the overall histogram fewer\
            than 'mm' times.
        probability: Convert each count to a probability by dividing by the\
            total number of counts at each voxel.
        quiet: Stop the highly informative progress reports.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLocalHistog",
        "prefix": prefix,
        "exc_nonlab": exc_nonlab,
        "probability": probability,
        "quiet": quiet,
        "input_datasets": input_datasets,
    }
    if nbhd_option is not None:
        params["nbhd_option"] = nbhd_option
    if hsave is not None:
        params["hsave"] = hsave
    if lab_file is not None:
        params["lab_file"] = lab_file
    if exclude is not None:
        params["exclude"] = exclude
    if mincount is not None:
        params["mincount"] = mincount
    return params


def v_3d_local_histog_cargs(
    params: V3dLocalHistogParameters,
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
    cargs.append("3dLocalHistog")
    if params.get("nbhd_option") is not None:
        cargs.extend([
            "-nbhd",
            params.get("nbhd_option")
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("hsave") is not None:
        cargs.extend([
            "-hsave",
            params.get("hsave")
        ])
    if params.get("lab_file") is not None:
        cargs.extend([
            "-lab_file",
            execution.input_file(params.get("lab_file"))
        ])
    if params.get("exclude") is not None:
        cargs.extend([
            "-exclude",
            *params.get("exclude")
        ])
    if params.get("exc_nonlab"):
        cargs.append("-excNONLAB")
    if params.get("mincount") is not None:
        cargs.extend([
            "-mincount",
            str(params.get("mincount"))
        ])
    if params.get("probability"):
        cargs.append("-prob")
    if params.get("quiet"):
        cargs.append("-quiet")
    cargs.extend([execution.input_file(f) for f in params.get("input_datasets")])
    return cargs


def v_3d_local_histog_outputs(
    params: V3dLocalHistogParameters,
    execution: Execution,
) -> V3dLocalHistogOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLocalHistogOutputs(
        root=execution.output_file("."),
        output_dataset_head=execution.output_file(params.get("prefix") + "+orig.HEAD"),
        output_dataset_brik=execution.output_file(params.get("prefix") + "+orig.BRIK"),
        histogram_file=execution.output_file(params.get("hsave")) if (params.get("hsave") is not None) else None,
    )
    return ret


def v_3d_local_histog_execute(
    params: V3dLocalHistogParameters,
    execution: Execution,
) -> V3dLocalHistogOutputs:
    """
    This program computes a local histogram at each voxel in the input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLocalHistogOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_local_histog_cargs(params, execution)
    ret = v_3d_local_histog_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_local_histog(
    prefix: str,
    input_datasets: list[InputPathType],
    nbhd_option: str | None = None,
    hsave: str | None = None,
    lab_file: InputPathType | None = None,
    exclude: list[str] | None = None,
    exc_nonlab: bool = False,
    mincount: float | None = None,
    probability: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dLocalHistogOutputs:
    """
    This program computes a local histogram at each voxel in the input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Use string 'ppp' as the prefix for the output dataset.
        input_datasets: Input dataset(s) for the 3dLocalHistog tool.
        nbhd_option: Defines the region around each voxel to be used for the\
            statistics calculation. Available formats: 'SPHERE(r)', 'RECT(a,b,c)',\
            'RHDD(a)', 'TOHD(a)'.
        hsave: Save the overall histogram into file 'sss'. This file will have\
            2 columns: value and count.
        lab_file: Use file 'LL' as a label file.
        exclude: Exclude values from 'a' to 'b' from the counting. This option\
            can be used more than once.
        exc_nonlab: If '-lab_file' is used, then exclude all values that are\
            NOT in the label file (except for 0).
        mincount: Exclude values which appear in the overall histogram fewer\
            than 'mm' times.
        probability: Convert each count to a probability by dividing by the\
            total number of counts at each voxel.
        quiet: Stop the highly informative progress reports.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalHistogOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_HISTOG_METADATA)
    params = v_3d_local_histog_params(
        nbhd_option=nbhd_option,
        prefix=prefix,
        hsave=hsave,
        lab_file=lab_file,
        exclude=exclude,
        exc_nonlab=exc_nonlab,
        mincount=mincount,
        probability=probability,
        quiet=quiet,
        input_datasets=input_datasets,
    )
    return v_3d_local_histog_execute(params, execution)


__all__ = [
    "V3dLocalHistogOutputs",
    "V3dLocalHistogParameters",
    "V_3D_LOCAL_HISTOG_METADATA",
    "v_3d_local_histog",
    "v_3d_local_histog_params",
]
