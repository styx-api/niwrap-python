# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_RF_TRAIN_METADATA = Metadata(
    id="ed47732236da2816714345ea0516a2a3309483a8.boutiques",
    name="mris_rf_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisRfTrainParameters = typing.TypedDict('MrisRfTrainParameters', {
    "__STYXTYPE__": typing.Literal["mris_rf_train"],
    "subjects": list[str],
    "output_name": str,
    "hemi": typing.NotRequired[str | None],
    "surf": typing.NotRequired[str | None],
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
        "mris_rf_train": mris_rf_train_cargs,
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


class MrisRfTrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_rf_train(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_rf_train_params(
    subjects: list[str],
    output_name: str,
    hemi: str | None = None,
    surf: str | None = None,
) -> MrisRfTrainParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subjects to process.
        output_name: Output name for the trained model.
        hemi: Process specified hemisphere instead of the default 'lh'.
        surf: Change the default surface name from 'white' to the specified\
            surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_rf_train",
        "subjects": subjects,
        "output_name": output_name,
    }
    if hemi is not None:
        params["hemi"] = hemi
    if surf is not None:
        params["surf"] = surf
    return params


def mris_rf_train_cargs(
    params: MrisRfTrainParameters,
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
    cargs.append("mris_rf_train")
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_name"))
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("surf") is not None:
        cargs.extend([
            "--surf",
            params.get("surf")
        ])
    return cargs


def mris_rf_train_outputs(
    params: MrisRfTrainParameters,
    execution: Execution,
) -> MrisRfTrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRfTrainOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_rf_train_execute(
    params: MrisRfTrainParameters,
    execution: Execution,
) -> MrisRfTrainOutputs:
    """
    Tool for training a random forest classifier using MRIS surface data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRfTrainOutputs`).
    """
    params = execution.params(params)
    cargs = mris_rf_train_cargs(params, execution)
    ret = mris_rf_train_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_rf_train(
    subjects: list[str],
    output_name: str,
    hemi: str | None = None,
    surf: str | None = None,
    runner: Runner | None = None,
) -> MrisRfTrainOutputs:
    """
    Tool for training a random forest classifier using MRIS surface data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subjects to process.
        output_name: Output name for the trained model.
        hemi: Process specified hemisphere instead of the default 'lh'.
        surf: Change the default surface name from 'white' to the specified\
            surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRfTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_RF_TRAIN_METADATA)
    params = mris_rf_train_params(
        subjects=subjects,
        output_name=output_name,
        hemi=hemi,
        surf=surf,
    )
    return mris_rf_train_execute(params, execution)


__all__ = [
    "MRIS_RF_TRAIN_METADATA",
    "MrisRfTrainOutputs",
    "MrisRfTrainParameters",
    "mris_rf_train",
    "mris_rf_train_params",
]
