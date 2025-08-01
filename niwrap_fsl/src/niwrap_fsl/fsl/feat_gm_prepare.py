# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FEAT_GM_PREPARE_METADATA = Metadata(
    id="0f3a100ea6a5dad8243d8f86fcdda9779bdb4c4f.boutiques",
    name="feat_gm_prepare",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FeatGmPrepareParameters = typing.TypedDict('FeatGmPrepareParameters', {
    "__STYXTYPE__": typing.Literal["feat_gm_prepare"],
    "gm_output": str,
    "feat_dirs_list": list[InputPathType],
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
        "feat_gm_prepare": feat_gm_prepare_cargs,
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
    }.get(t)


class FeatGmPrepareOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat_gm_prepare(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def feat_gm_prepare_params(
    gm_output: str,
    feat_dirs_list: list[InputPathType],
) -> FeatGmPrepareParameters:
    """
    Build parameters.
    
    Args:
        gm_output: 4D grey matter output file.
        feat_dirs_list: List of first-level FEAT output directories.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "feat_gm_prepare",
        "gm_output": gm_output,
        "feat_dirs_list": feat_dirs_list,
    }
    return params


def feat_gm_prepare_cargs(
    params: FeatGmPrepareParameters,
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
    cargs.append("feat_gm_prepare")
    cargs.append(params.get("gm_output"))
    cargs.extend([execution.input_file(f) for f in params.get("feat_dirs_list")])
    return cargs


def feat_gm_prepare_outputs(
    params: FeatGmPrepareParameters,
    execution: Execution,
) -> FeatGmPrepareOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FeatGmPrepareOutputs(
        root=execution.output_file("."),
    )
    return ret


def feat_gm_prepare_execute(
    params: FeatGmPrepareParameters,
    execution: Execution,
) -> FeatGmPrepareOutputs:
    """
    Prepare 4D grey matter files for higher-level analysis in FEAT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FeatGmPrepareOutputs`).
    """
    params = execution.params(params)
    cargs = feat_gm_prepare_cargs(params, execution)
    ret = feat_gm_prepare_outputs(params, execution)
    execution.run(cargs)
    return ret


def feat_gm_prepare(
    gm_output: str,
    feat_dirs_list: list[InputPathType],
    runner: Runner | None = None,
) -> FeatGmPrepareOutputs:
    """
    Prepare 4D grey matter files for higher-level analysis in FEAT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        gm_output: 4D grey matter output file.
        feat_dirs_list: List of first-level FEAT output directories.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FeatGmPrepareOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT_GM_PREPARE_METADATA)
    params = feat_gm_prepare_params(
        gm_output=gm_output,
        feat_dirs_list=feat_dirs_list,
    )
    return feat_gm_prepare_execute(params, execution)


__all__ = [
    "FEAT_GM_PREPARE_METADATA",
    "FeatGmPrepareOutputs",
    "FeatGmPrepareParameters",
    "feat_gm_prepare",
    "feat_gm_prepare_params",
]
