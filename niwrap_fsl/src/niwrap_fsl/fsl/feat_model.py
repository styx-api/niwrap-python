# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FEAT_MODEL_METADATA = Metadata(
    id="e1b97eac6407023b70ba9603b867c2c4df4235a1.boutiques",
    name="feat_model",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FeatModelParameters = typing.TypedDict('FeatModelParameters', {
    "__STYXTYPE__": typing.Literal["feat_model"],
    "design_name_root": str,
    "confound_matrix": typing.NotRequired[InputPathType | None],
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
        "feat_model": feat_model_cargs,
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


class FeatModelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `feat_model(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def feat_model_params(
    design_name_root: str,
    confound_matrix: InputPathType | None = None,
) -> FeatModelParameters:
    """
    Build parameters.
    
    Args:
        design_name_root: Design name root.
        confound_matrix: Confound matrix text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "feat_model",
        "design_name_root": design_name_root,
    }
    if confound_matrix is not None:
        params["confound_matrix"] = confound_matrix
    return params


def feat_model_cargs(
    params: FeatModelParameters,
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
    cargs.append("feat_model")
    cargs.append(params.get("design_name_root"))
    if params.get("confound_matrix") is not None:
        cargs.append(execution.input_file(params.get("confound_matrix")))
    return cargs


def feat_model_outputs(
    params: FeatModelParameters,
    execution: Execution,
) -> FeatModelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FeatModelOutputs(
        root=execution.output_file("."),
    )
    return ret


def feat_model_execute(
    params: FeatModelParameters,
    execution: Execution,
) -> FeatModelOutputs:
    """
    Generate design matrices for use by FEAT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FeatModelOutputs`).
    """
    params = execution.params(params)
    cargs = feat_model_cargs(params, execution)
    ret = feat_model_outputs(params, execution)
    execution.run(cargs)
    return ret


def feat_model(
    design_name_root: str,
    confound_matrix: InputPathType | None = None,
    runner: Runner | None = None,
) -> FeatModelOutputs:
    """
    Generate design matrices for use by FEAT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        design_name_root: Design name root.
        confound_matrix: Confound matrix text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FeatModelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEAT_MODEL_METADATA)
    params = feat_model_params(
        design_name_root=design_name_root,
        confound_matrix=confound_matrix,
    )
    return feat_model_execute(params, execution)


__all__ = [
    "FEAT_MODEL_METADATA",
    "FeatModelOutputs",
    "FeatModelParameters",
    "feat_model",
    "feat_model_params",
]
